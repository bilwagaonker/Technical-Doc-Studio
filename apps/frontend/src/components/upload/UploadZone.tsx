"use client";

import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { UploadCloud, Loader2 } from "lucide-react";
import { uploadVideo } from "@/lib/api";
import { PipelineStatus } from "../pipeline/PipelineCard";

interface UploadZoneProps {
  setPipelineStatus: (status: PipelineStatus) => void;
}

export default function UploadZone({
  setPipelineStatus,
}: UploadZoneProps) {
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const onDrop = useCallback(
    async (acceptedFiles: File[]) => {
      if (acceptedFiles.length === 0) return;

      const file = acceptedFiles[0];

      try {
        setUploading(true);

        setPipelineStatus("uploaded");
        setMessage("📤 Video uploaded successfully.");

        // Small delay so user can see the Uploaded state
        await new Promise((resolve) => setTimeout(resolve, 500));

        setPipelineStatus("processing");
        setMessage("⚙️ AI is processing your SAP demo video...");

        const result = await uploadVideo(file);

        console.log(result.downloads);

        setPipelineStatus("completed");
        setMessage("✅ Documentation is ready for download.");

      } catch (error: any) {
        console.error(error);

        setPipelineStatus("uploaded");

        setMessage(
          error?.message || "❌ Failed to generate documentation."
        );
      } finally {
        setUploading(false);
      }
    },
    [setPipelineStatus]
  );

  const {
    getRootProps,
    getInputProps,
    isDragActive,
  } = useDropzone({
    onDrop,
    multiple: false,
    disabled: uploading,
    accept: {
      "video/mp4": [".mp4"],
      "video/x-msvideo": [".avi"],
      "video/quicktime": [".mov"],
      "video/x-matroska": [".mkv"],
    },
  });

  return (
    <div
      {...getRootProps()}
      className={`rounded-xl border-2 border-dashed p-12 cursor-pointer transition
      ${
        isDragActive
          ? "border-blue-600 bg-blue-50"
          : "border-slate-300 bg-white hover:border-blue-500"
      }`}
    >
      <input {...getInputProps()} />

      <div className="flex flex-col items-center">
        {uploading ? (
          <Loader2 className="h-16 w-16 animate-spin text-blue-600" />
        ) : (
          <UploadCloud className="h-16 w-16 text-blue-600" />
        )}

        <h2 className="mt-4 text-2xl font-semibold">
          Upload SAP Demo Video
        </h2>

        <p className="mt-2 text-center text-slate-500">
          {uploading
            ? "Processing your video..."
            : isDragActive
            ? "Drop the video here..."
            : "Drag & Drop your SAP demo video or click to browse"}
        </p>

        <div className="mt-6 flex gap-2">
          {["MP4", "AVI", "MOV", "MKV"].map((format) => (
            <span
              key={format}
              className="rounded bg-slate-100 px-3 py-1 text-sm"
            >
              {format}
            </span>
          ))}
        </div>

        {message && (
          <div className="mt-6 rounded-lg bg-slate-100 px-4 py-3 text-center text-sm text-slate-700">
            {message}
          </div>
        )}
      </div>
    </div>
  );
}