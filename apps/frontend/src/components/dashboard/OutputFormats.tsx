"use client";

import {
  FileText,
  FileSpreadsheet,
  Globe,
  FileCode2,
  Download,
} from "lucide-react";

interface OutputFormatsProps {
  downloads?: {
    docx?: string;
    pdf?: string;
    html?: string;
    markdown?: string;
  };
}

export default function OutputFormats({
  downloads,
}: OutputFormatsProps) {
  const files = [
    {
      name: "DOCX",
      description: "Quick Reference Guide",
      icon: FileText,
      url: downloads?.docx,
    },
    {
      name: "PDF",
      description: "Printable Document",
      icon: FileSpreadsheet,
      url: downloads?.pdf,
    },
    {
      name: "HTML",
      description: "Knowledge Portal",
      icon: Globe,
      url: downloads?.html,
    },
    {
      name: "Markdown",
      description: "GitHub Documentation",
      icon: FileCode2,
      url: downloads?.markdown,
    },
  ];

  return (
    <div className="rounded-xl border bg-white shadow-sm h-full">
      <div className="border-b p-5">
        <h2 className="text-xl font-semibold">
          Output Formats
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Download the generated documentation.
        </p>
      </div>

      <div className="grid grid-cols-2 gap-4 p-5">
        {files.map((file) => {
          const Icon = file.icon;

          const enabled = !!file.url;

          return enabled ? (
            <a
              key={file.name}
              href={`http://localhost:8000${file.url}`}
              download
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-lg border p-4 hover:border-blue-500 hover:bg-blue-50 transition"
            >
              <Icon className="h-8 w-8 text-blue-600" />

              <h3 className="mt-3 font-semibold">
                {file.name}
              </h3>

              <p className="mt-1 text-sm text-slate-500">
                {file.description}
              </p>

              <div className="mt-4 flex items-center gap-2 text-blue-600 text-sm font-medium">
                <Download className="h-4 w-4" />
                Download
              </div>
            </a>
          ) : (
            <div
              key={file.name}
              className="rounded-lg border border-slate-200 bg-slate-50 p-4 opacity-50 cursor-not-allowed"
            >
              <Icon className="h-8 w-8 text-slate-400" />

              <h3 className="mt-3 font-semibold text-slate-500">
                {file.name}
              </h3>

              <p className="mt-1 text-sm text-slate-400">
                {file.description}
              </p>

              <div className="mt-4 text-xs text-slate-400">
                Not generated yet
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}