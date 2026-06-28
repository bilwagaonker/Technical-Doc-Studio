"use client";

import {useCallback} from "react";
import {useDropzone} from "react-dropzone";
import {UploadCloud} from "lucide-react";

export default function UploadZone() {

    const onDrop = useCallback((acceptedFiles: File[]) => {

        console.log(acceptedFiles);

    }, []);

    const {getRootProps,getInputProps,isDragActive}=useDropzone({

        onDrop,

        multiple:false,

        accept:{
            "video/mp4":[".mp4"],
            "video/x-msvideo":[".avi"],
            "video/quicktime":[".mov"],
            "video/x-matroska":[".mkv"]
        }

    });

    return(

        <div
        {...getRootProps()}
        className="rounded-xl border-2 border-dashed border-slate-300 bg-white p-12 cursor-pointer hover:border-blue-500 transition"
        >

            <input {...getInputProps()} />

            <div className="flex flex-col items-center">

                <UploadCloud className="h-16 w-16 text-blue-600"/>

                <h2 className="mt-4 text-2xl font-semibold">
                    Upload SAP Demo Video
                </h2>

                <p className="mt-2 text-slate-500">

                    {isDragActive
                    ? "Drop the video here..."
                    : "Drag & Drop your demo video or click to browse"}

                </p>

                <div className="mt-6 flex gap-2">

                    <span className="rounded bg-slate-100 px-3 py-1 text-sm">
                        MP4
                    </span>

                    <span className="rounded bg-slate-100 px-3 py-1 text-sm">
                        AVI
                    </span>

                    <span className="rounded bg-slate-100 px-3 py-1 text-sm">
                        MOV
                    </span>

                    <span className="rounded bg-slate-100 px-3 py-1 text-sm">
                        MKV
                    </span>

                </div>

            </div>

        </div>

    )

}