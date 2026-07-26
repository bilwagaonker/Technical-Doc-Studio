"use client";

import {
  Upload,
 LoaderCircle,
  Download,
  CheckCircle2,
  Circle,
} from "lucide-react";

type StepState = "waiting" | "processing" | "done";

interface Step {
  title: string;
  icon: React.ElementType;
  state: StepState;
}
export type PipelineStatus =
  | "idle"
  | "uploaded"
  | "processing"
  | "completed";

interface Props {
  status: PipelineStatus;
}

export default function PipelineCard({ status }: Props) {
  const steps :Step[] = [
    {
      title: "Video Uploaded",
      icon: Upload,
      state:
        status === "idle"
          ? "waiting"
          : "done",
    },

    {
      title: "AI Processing",
      icon: LoaderCircle,
      state:
        status === "processing"
          ? "processing"
          : status === "completed"
          ? "done"
          : "waiting",
    },

    {
      title: "Ready for Download",
      icon: Download,
      state:
        status === "completed"
          ? "done"
          : "waiting",
    },
  ];

  return (
    <div className="rounded-xl border bg-white shadow-sm">

      <div className="border-b p-5">
        <h2 className="text-xl font-semibold">
          AI Processing Pipeline
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Monitor the documentation generation process.
        </p>
      </div>

      <div className="p-6 space-y-6">

        {steps.map((step) => {

          const Icon = step.icon;

          return (

            <div
              key={step.title}
              className="flex items-center justify-between"
            >

              <div className="flex items-center gap-4">

                <div
                  className={`rounded-full p-2 ${
                    step.state === "waiting"
                      ? "bg-slate-100"
                      : "bg-blue-100"
                  }`}
                >

                  <Icon
                    className={`h-5 w-5
                      ${
                        step.state === "waiting"
                          ? "text-slate-400"
                          : "text-blue-600"
                      }
                      ${
                        step.state === "processing"
                          ? "animate-spin"
                          : ""
                      }
                    `}
                  />

                </div>

                <span className="font-medium">
                  {step.title}
                </span>

              </div>

              <StatusBadge status={step.state} />

            </div>

          );

        })}

      </div>

    </div>
  );
}

function StatusBadge({
  status,
}: {
  status: "waiting" | "processing" | "done";
}) {

  if (status === "processing") {

    return (
      <div className="flex items-center gap-2 text-blue-600">
        <LoaderCircle className="h-4 w-4 animate-spin" />
        <span className="text-sm">
          Processing
        </span>
      </div>
    );

  }

  if (status === "done") {

    return (
      <div className="flex items-center gap-2 text-green-600">
        <CheckCircle2 className="h-4 w-4" />
        <span className="text-sm">
          Done
        </span>
      </div>
    );

  }

  return (
    <div className="flex items-center gap-2 text-slate-400">
      <Circle className="h-4 w-4" />
      <span className="text-sm">
        Waiting
      </span>
    </div>
  );
}