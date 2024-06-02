import CustomTable from '@/components/custom-table'
import React from 'react'
import { Coursebuttons, Sessiondata } from '../constant'

const ViewSession = () => {
  return (
    <div className='flex justify-center items-center'>
     <CustomTable data={Sessiondata} buttons={Coursebuttons} additionalHeadings={['View Session Data']} />
    </div>
  )
}

export default ViewSession
