
"use client"
import React from 'react';
import CustomTable from "@/components/custom-table";
import { Teacherdata, Teacherbuttons } from "../constant";
import { useRouter } from "next/navigation";

const ViewTeachers = () => {
    const router = useRouter();

    // Define the handleEditClick function to handle navigation to the edit section
    const handleEditClick = () => {
        router.push('/teacher/edit');
    };

    // Dynamically assign the onClick callback for the edit button
    const dynamicTeacherButtons = Teacherbuttons.map(button => {
        if (button.label === 'Edit') {
            return { ...button, onClick: handleEditClick }; // Assign the handleEditClick function
        }
        return button;
    });

    return (
        <div className='flex justify-center items-center'>
            <CustomTable data={Teacherdata} buttons={dynamicTeacherButtons} additionalHeadings={['View Teachers Data']} />
        </div>
    );
};

export default ViewTeachers;
