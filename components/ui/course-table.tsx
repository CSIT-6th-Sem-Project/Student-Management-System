import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table"
 
  
  import React from 'react'
  
  const CourseTable = () => {
    return (
        <Table>
        <TableCaption>A list of record of courses</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[100px]">#</TableHead>
            <TableHead className="w-[100px]">Course Name</TableHead>
            <TableHead className="w-[100px]">Action</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell className="font-medium">INV001</TableCell>
            <TableCell>Bsc.CSIT</TableCell>
            <TableCell>Edit,delete</TableCell>
          </TableRow>
        </TableBody>
      </Table>
      
    )
  }
  
  export default CourseTable
  