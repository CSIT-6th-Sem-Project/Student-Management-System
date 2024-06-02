import CustomTable from '@/components/custom-table'
import React from 'react'
import { Coursebuttons, Coursedata, Studentdata } from '../constant'

const ViewStudent = () => {
  return (
   <div className='flex justify-center items-center'>
     <CustomTable data={Studentdata} buttons={Coursebuttons}  additionalHeadings={['View Student Data']}/>
    </div>
  )
}

export default ViewStudent
