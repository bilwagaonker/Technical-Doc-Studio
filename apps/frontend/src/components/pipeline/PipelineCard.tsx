"use client";

import {
  Upload,
  Image,
  ScanText,
  MonitorSmartphone,
  Mic,
  BrainCircuit,
  FileOutput,
  Circle,
  CheckCircle2,
  LoaderCircle,
} from "lucide-react";

type Status = "waiting" | "running" | "completed";

interface PipelineStep {
  name: string;
  icon: React.ElementType;
  status: Status;
}

const steps: PipelineStep[] = [
  {
    name: "Upload Video",
    icon: Upload,
    status: "completed",
  },
  {
    name: "Extract Frames",
    icon: Image,
    status: "waiting",
  },
  {
    name: "OCR & Layout Analysis",
    icon: ScanText,
    status: "waiting",
  },
  {
    name: "SAP UI Detection",
    icon: MonitorSmartphone,
    status: "waiting",
  },
  {
    name: "Speech Transcription",
    icon: Mic,
    status: "waiting",
  },
  {
    name: "AI Documentation",
    icon: BrainCircuit,
    status: "waiting",
  },
  {
    name: "Generate Documents",
    icon: FileOutput,
    status: "waiting",
  },
];

export default function PipelineCard() {
  return (
    <div className="rounded-xl border bg-white shadow-sm">
      <div className="border-b p-5">
        <h2 className="text-xl font-semibold">
          AI Processing Pipeline
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Real-time execution of the documentation engine.
        </p>
      </div>

      <div className="p-5 space-y-5">
        {steps.map((step) => {
          const Icon = step.icon;

          return (
            <div
              key={step.name}
              className="flex items-center justify-between"
            >
              <div className="flex items-center gap-4">
                <Icon className="h-5 w-5 text-blue-600" />

                <span>{step.name}</span>
              </div>

              <StatusIcon status={step.status} />
            </div>
          );
        })}
      </div>
    </div>
  );
}

function StatusIcon({
  status,
}: {
  status: Status;
}) {
  switch (status) {
    case "completed":
      return (
        <div className="flex items-center gap-2 text-green-600">
          <CheckCircle2 className="h-5 w-5" />
          <span className="text-sm">Done</span>
        </div>
      );

    case "running":
      return (
        <div className="flex items-center gap-2 text-blue-600">
          <LoaderCircle className="h-5 w-5 animate-spin" />
          <span className="text-sm">Running</span>
        </div>
      );

    default:
      return (
        <div className="flex items-center gap-2 text-slate-400">
          <Circle className="h-4 w-4" />
          <span className="text-sm">Waiting</span>
        </div>
      );
  }
}