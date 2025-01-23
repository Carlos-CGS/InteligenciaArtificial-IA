from pathlib import Path

import boto3
from mypy_boto3_rekognition.type_defs import CompareFacesMatchTypeDef
from PIL import Image, ImageDraw

client = boto3.client("rekognition")


def get_path(file_name: str) -> str:
    return str(Path(__file__).parent / "images" / file_name)


def compare_faces(
    source_image_path: str, target_image_path: str, similarity_threshold: int = 80
):
    with open(source_image_path, "rb") as source_image, open(
        target_image_path, "rb"
    ) as target_image:
        response = client.compare_faces(
            SourceImage={"Bytes": source_image.read()},
            TargetImage={"Bytes": target_image.read()},
            SimilarityThreshold=similarity_threshold,
        )
    return response


def draw_boxes(
    image_path: str, output_path: str, face_details: list[CompareFacesMatchTypeDef]
) -> None:
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    width, height = image.size

    for face in face_details:
        box = face["Face"]["BoundingBox"]  # type: ignore
        left = int(box["Left"] * width)  # type: ignore
        top = int(box["Top"] * height)  # type: ignore
        right = int((box["Left"] + box["Width"]) * width)  # type: ignore
        bottom = int((box["Top"] + box["Height"]) * height)  # type: ignore

        draw.rectangle([left, top, right, bottom], outline="red", width=3)

        similarity = face["Similarity"]  # type: ignore
        draw.text((left, top - 10), f"{similarity:.1f}%", fill="red")

    image.save(output_path)
    print(f"Imagem salva com resultados em: {output_path}")


if __name__ == "__main__":
    source_image_path = get_path("neymar.jpg")
    target_image_path = get_path("msn.jpg")
    output_image_path = get_path("resultado_msn.jpg")
    response = compare_faces(source_image_path, target_image_path)

    if response["FaceMatches"]:
        print("Rostos encontrados: ")
        for match in response["FaceMatches"]:
            print(f"- Similaridade: {match['Similarity']:.2f}")  # type: ignore

        draw_boxes(target_image_path, output_image_path, response["FaceMatches"])
    else:
        print("Nenhum rosto correspondente foi encontrado.")
