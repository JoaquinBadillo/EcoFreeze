interface DashboardProps {
    children: React.ReactNode;
}

const Dashboard = (props: DashboardProps) => (
    <div className="flex flex-wrap gap-4 mx-auto p-16">
        <div className="w-full"><h1 className="text-4xl font-bold text-center">EcoFreeze Dashboard</h1></div>
        {props.children}
    </div>
);

export default Dashboard;