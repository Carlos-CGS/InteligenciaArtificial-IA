from pathlib import Path

import boto3
from mypy_boto3_rekognition.type_defs import (
    CelebrityTypeDef,
    RecognizeCelebritiesResponseTypeDef,
)
from PIL import Image, ImageDraw, ImageFont

client = boto3.client("rekognition")


def get_path(file_name: str) -> str:
    return str(Path(__file__).parent / "images" / file_name)


def recognize_celebrities(photo: str) -> RecognizeCelebritiesResponseTypeDef:
    with open(photo, "rb") as image:
        return client.recognize_celebrities(Image={"Bytes": image.read()})


def draw_boxes(image_path: str, output_path: str, face_details: list[CelebrityTypeDef]):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Ubuntu-R.ttf", 20)

    width, height = image.size

    for face in face_details:
        box = face["Face"]["BoundingBox"]  # type: ignore
        left = int(box["Left"] * width)  # type: ignore
        top = int(box["Top"] * height)  # type: ignore
        right = int((box["Left"] + box["Width"]) * width)  # type: ignore
        bottom = int((box["Top"] + box["Height"]) * height)  # type: ignore

        confidence = face.get("MatchConfidence", 0)
        if confidence > 90:
            draw.rectangle([left, top, right, bottom], outline="red", width=3)

            text = face.get("Name", "")
            position = (left, top - 20)
            bbox = draw.textbbox(position, text, font=font)
            draw.rectangle(bbox, fill="red")
            draw.text(position, text, font=font, fill="white")

    image.save(output_path)
    print(f"Imagem salva com resultados em : {output_path}")


if __name__ == "__main__":
    photo_paths = [
        get_path("bbc.jpg"),
        get_path("msn.jpg"),
        get_path("neymar-torcedores.jpg"),
    ]

    for photo_path in photo_paths:
        response = recognize_celebrities(photo_path)
        faces = response["CelebrityFaces"]
        if not faces:
            print(f"Não foram encontrados famosos para a imagem: {photo_path}")
            continue
        output_path = get_path(f"{Path(photo_path).stem}-resultado.jpg")
        draw_boxes(photo_path, output_path, faces)
