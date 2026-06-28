export default function Navbar() {
  return (
    <nav className="border-b bg-white">
      <div className="mx-auto max-w-7xl px-6 py-4 flex items-center justify-between">
        <h1 className="text-xl font-bold">
          AI Technical Documentation Studio
        </h1>

        <div className="flex gap-6 text-sm">
          <button>Home</button>
          <button>Jobs</button>
          <button>Settings</button>
        </div>
      </div>
    </nav>
  );
}