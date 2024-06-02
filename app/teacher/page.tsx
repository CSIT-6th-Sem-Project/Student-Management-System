import CustomTable from "@/components/custom-table"
import { Coursebuttons, Coursedata, Teacherbuttons, Teacherdata } from "../constant"


const ViewTeachers = () => {
    return (
      <div className='flex justify-center items-center'>
 <CustomTable data={Teacherdata} buttons={Teacherbuttons}  additionalHeadings={['View Teachers Data']} />
      </div>
    )
  }
  
  export default ViewTeachers
  