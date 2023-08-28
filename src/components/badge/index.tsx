interface BadgeProps {
    icon: React.ReactNode;
    label: string;
    value: number | string;
    color: 'red' | 'green' | 'purple' | 'yellow' | 'blue';
}

const Badge = ({icon, value, label, color}: BadgeProps) => {
    const colorMap = {
        'red': 'bg-red-300',
        'green': 'bg-green-300',
        'purple': 'bg-purple-300',
        'yellow': 'bg-yellow-300',
        'blue': 'bg-blue-300'
    };

    return (
        <div className="flex flex-row rounded-lg shadow-xl m-5 w-60 h-20">
            <span className={`rounded-full ${colorMap[color]} text-xl p-2 m-4`}>{icon}</span>
            <div className="flex flex-col justify-center items-start m-3">
                <span className="text-xs text-gray-800">{label}</span>
                <span className="text-2xl">{value}</span>
            </div>
        </div>
    );
}

export default Badge;