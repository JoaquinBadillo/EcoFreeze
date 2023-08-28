import Badge from '../badge';
import { BsThermometerLow } from 'react-icons/bs';

export const DesiredTemperature = () => {
    return (
        <Badge 
            icon={<BsThermometerLow size={30}/>} 
            value={"18 °C"}
            label={"Desired Temperature"}
        color='purple'/>
    );
}

export const RoomTemperature = () => {
    return (
        <Badge 
            icon={<BsThermometerLow size={30}/>} 
            value={"19 °C"}
            label={"Room Temperature"}
        color='yellow'/>
    );
}

export const ExternalTemperature = () => {
    return (
        <Badge 
            icon={<BsThermometerLow size={30}/>} 
            value={"24 °C"}
            label={"External Temperature"}
        color='blue'/>
    );
}

const TemperatureBadges = () => {
    return (
        <div className="flex flex-row w-full">
            <DesiredTemperature />
            <RoomTemperature />
            <ExternalTemperature />
        </div>
    );
}

export default TemperatureBadges;
