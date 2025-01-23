import json
from pathlib import Path
from typing import Dict, List, Tuple

import boto3
from mypy_boto3_textract.type_defs import BlockTypeDef


def get_document_data(file_name: str) -> bytearray:
    with open(file_name, "rb") as file:
        img = file.read()
        doc_bytes = bytearray(img)
        print(f"Imagem carregada {file_name}")
    return doc_bytes


def analyze_document() -> None:
    client = boto3.client("textract")
    file_path = str(Path(__file__).parent / "images" / "cnh.png")
    doc_bytes = get_document_data(file_path)
    response = client.analyze_document(
        Document={"Bytes": doc_bytes},  # type: ignore
        FeatureTypes=["FORMS"],
    )
    with open("response.json", "w") as response_file:
        response_file.write(json.dumps(response))


def get_kv_map() -> Tuple[Dict[str, Dict], Dict[str, Dict], Dict[str, Dict]]:
    key_map: Dict[str, Dict] = {}
    value_map: Dict[str, Dict] = {}
    block_map: Dict[str, Dict] = {}
    blocks: List[BlockTypeDef] = []

    try:
        with open("response.json", "r") as file:
            blocks = json.loads(file.read())["Blocks"]
    except IOError:
        analyze_document()

    for block in blocks:
        block_id = block["Id"]  # type: ignore
        block_map[block_id] = block  # type: ignore
        if block["BlockType"] == "KEY_VALUE_SET":  # type: ignore
            if "KEY" in block["EntityTypes"]:  # type: ignore
                key_map[block_id] = block  # type: ignore
            else:
                value_map[block_id] = block  # type: ignore

    return key_map, value_map, block_map


def get_kv_relationship(
    key_map: Dict[str, Dict], value_map: Dict[str, Dict], block_map: Dict[str, Dict]
) -> Dict:
    kvs = {}
    for _, key_block in key_map.items():
        value_block = find_value_block(key_block, value_map)
        key = get_text(key_block, block_map)
        value = get_text(value_block, block_map)
        kvs[key] = value
    return kvs


def find_value_block(
    key_block: Dict[str, Dict], value_map: Dict[str, Dict]
) -> Dict[str, Dict]:
    for relationship in key_block.get("Relationships", []):
        if relationship["Type"] == "VALUE":
            for value_id in relationship["Ids"]:
                return value_map[value_id]
    return {}


def get_text(result: Dict[str, Dict], block_map: Dict[str, Dict]) -> str:
    text = ""
    if "Relationships" in result:
        for relationship in result["Relationships"]:
            if relationship["Type"] == "CHILD":
                for child_id in relationship["Ids"]:
                    word = block_map[child_id]
                    if word["BlockType"] == "WORD":
                        text += word["Text"] + " "
    return text.rstrip()


if __name__ == "__main__":
    key_map, value_map, block_map = get_kv_map()
    kvs = get_kv_relationship(key_map, value_map, block_map)

    print("\n\n== DADOS DA CNH ==\n\n")
    for k, v in kvs.items():
        print(f"{k}: {v}")
