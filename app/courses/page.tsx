import CustomTable from '@/components/custom-table';
import React from 'react';
import { Coursebuttons, Coursedata } from '../constant';


const CourseTable: React.FC = () => {

    return (
        <div className='flex justify-center items-center'>
    <CustomTable data={Coursedata} buttons={Coursebuttons}  additionalHeadings={['View Course Data']}/>
    </div>
    )
};

export default CourseTable;
