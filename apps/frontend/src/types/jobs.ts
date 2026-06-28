export type JobStatus =
  | "Queued"
  | "Processing"
  | "Completed"
  | "Failed";

export interface Job {
  id: string;
  fileName: string;
  uploadedAt: string;
  status: JobStatus;
  progress: number;
}