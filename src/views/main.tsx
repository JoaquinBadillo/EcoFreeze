import Dashboard from '../components/dashboard';
import EnergyUsage from '../components/energy-usage';
import CarbonEmissions from '../components/carbon-emissions';
import TemperatureBadges from '../components/temperature-badges';

function App() {
  return (
    <Dashboard>
        <TemperatureBadges />
        <EnergyUsage />
        <CarbonEmissions />
    </Dashboard>
  )
}

export default App