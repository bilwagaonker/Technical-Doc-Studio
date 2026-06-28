import UploadZone from "@/components/upload/UploadZone";
import PipelineCard from "@/components/pipeline/PipelineCard";
import RecentJobs from "@/components/dashboard/RecentJobs";
import OutputFormats from "@/components/dashboard/OutputFormats";

export default function Dashboard() {
  return (
    <div className="space-y-8">
      <section>
        <h2 className="text-4xl font-bold tracking-tight">
          Convert SAP Demo Videos into Documentation
        </h2>

        <p className="mt-3 max-w-3xl text-slate-600">
          Upload a demo video and let AI generate structured
          technical documentation, quick reference guides,
          business process procedures, and training material.
        </p>
      </section>

      <div className="grid gap-6 lg:grid-cols-2">
        <UploadZone/>

        <PipelineCard />

        <RecentJobs/>

        <OutputFormats />
      </div>
    </div>
  );
}