import { LineChart, Line, CartesianGrid, XAxis, YAxis, ResponsiveContainer, Label } from 'recharts';

const data = Array(24).fill(0).map((_, i) => (
    { time: `${i < 10 ? `0${i}`: i}:00`, energy: Math.floor(Math.random() * 1000) }
));

const Chart = () => (
  <div className='flex flex-col rounded-lg shadow-lg m-5 items-center w-5/12'>
    <h2 className='text-lg font-bold'>Energy Consumption</h2>
    <ResponsiveContainer width='90%' height={300}>
        <LineChart width={400} height={200} data={data} margin={{left: 30, right: 40, top: 20, bottom: 40}}>
            <Line type="monotone" dataKey="energy" strokeWidth={3} />
            <CartesianGrid stroke="#ccc" strokeDasharray="3 5" />
            <XAxis dataKey="time" dy={10}>
                <Label position='bottom' dy={10}>
                    Time
                </Label>
            </XAxis>
            <YAxis>
                <Label angle={270} position='left' style={{ textAnchor: 'middle' }}>
                    Energy (kWh)
                </Label>
            </YAxis>
        </LineChart>
    </ResponsiveContainer>
  </div>
);

export default Chart;