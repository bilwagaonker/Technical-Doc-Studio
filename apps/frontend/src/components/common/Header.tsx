import { Settings, FileText } from "lucide-react";

export default function Header() {
  return (
    <header className="border-b bg-white">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <FileText className="h-7 w-7 text-blue-600" />

          <div>
            <h1 className="text-lg font-bold">
              AI Technical Documentation Studio
            </h1>

            <p className="text-xs text-gray-500">
              AI-powered SAP Documentation Generator
            </p>
          </div>
        </div>

        <button className="rounded-lg border p-2 hover:bg-slate-100">
          <Settings className="h-5 w-5" />
        </button>
      </div>
    </header>
  );
}