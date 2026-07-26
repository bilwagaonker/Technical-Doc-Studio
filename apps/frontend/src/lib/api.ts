const API_URL = process.env.NEXT_PUBLIC_API_URL ||
    "http://127.0.0.1:8000";

export async function uploadVideo(file: File) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(`${API_URL}/upload`, {

        method: "POST",

        body: formData

    });

    if (!response.ok) {

        throw new Error(await response.text());

    }

    return await response.json();

}