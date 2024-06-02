import CustomTable from "@/components/custom-table"
import { Coursebuttons, Coursedata, Subjectdata } from "../constant"


const ViewSubject= () => {
    return (
      <div className='flex justify-center items-center'>
  <CustomTable data={Subjectdata} buttons={Coursebuttons}  additionalHeadings={['View Subject Data']} />
      </div>
    )
  }
  
  export default ViewSubject
  