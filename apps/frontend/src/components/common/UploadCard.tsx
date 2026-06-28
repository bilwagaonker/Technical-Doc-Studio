export default function UploadCard() {
  return (
    <div className="rounded-xl border p-8 shadow-sm bg-white">
      <h2 className="text-2xl font-semibold mb-4">
        Upload Demo Video
      </h2>

      <div className="border-2 border-dashed rounded-lg p-16 text-center">
        Drag & Drop Video Here
      </div>

      <div className="mt-6">
        <p className="font-medium">Supported Formats</p>

        <div className="flex gap-2 mt-2">
          <span>MP4</span>
          <span>AVI</span>
          <span>MOV</span>
          <span>MKV</span>
        </div>
      </div>
    </div>
  );
}