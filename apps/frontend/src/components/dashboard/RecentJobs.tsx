"use client";

import { Clock3, FileVideo, CircleDashed } from "lucide-react";
import type { Job } from "@/types/jobs";

const jobs: Job[] = [];

export default function RecentJobs() {
  return (
    <div className="rounded-xl border bg-white shadow-sm h-full">
      <div className="border-b p-5">
        <h2 className="text-xl font-semibold">Recent Jobs</h2>
        <p className="mt-1 text-sm text-slate-500">
          Previously processed documentation jobs.
        </p>
      </div>

      <div className="p-5">
        {jobs.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <CircleDashed className="h-12 w-12 text-slate-300" />

            <h3 className="mt-4 font-medium">
              No Jobs Yet
            </h3>

            <p className="mt-2 text-sm text-slate-500 max-w-xs">
              Upload your first SAP demonstration video to begin
              generating technical documentation.
            </p>
          </div>
        ) : (
          jobs.map((job) => (
            <div key={job.id}>
              <FileVideo />
            </div>
          ))
        )}
      </div>
    </div>
  );
}