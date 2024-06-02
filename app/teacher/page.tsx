import CustomTable from "@/components/custom-table"
import { Coursebuttons, Coursedata, Teacherdata } from "../constant"


const ViewTeachers = () => {
    return (
      <div className='flex justify-center items-center'>
 <CustomTable data={Teacherdata} buttons={Coursebuttons}  additionalHeadings={['View Teachers Data']} />
      </div>
    )
  }
  
  export default ViewTeachers
  