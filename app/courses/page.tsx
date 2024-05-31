"use client"

import React from 'react';
import { courses } from '../constant';


const ViewCourses: React.FC = () => {
  // Function to handle editing a course
  const handleEdit = (courseId: number) => {
    console.log(`Editing course with ID: ${courseId}`);
    // Implement your edit logic here
  };

  // Function to handle deleting a course
  const handleDelete = (courseId: number) => {
    console.log(`Deleting course with ID: ${courseId}`);
    // Implement your delete logic here
  };

  return (
    <div className="flex justify-center  h-screen">
      <div className="w-full lg:w-2/3 px-4 py-2">
        <h2 className="text-2xl font-bold mb-4">View Courses</h2>
        <table className="w-full border-collapse border border-gray-300">
          <thead>
            <tr className="bg-gray-100 text-black">
              <th className="border  border-gray-500 px-4 py-2">Course ID</th>
              <th className="border border-gray-500 px-4 py-2">Course Name</th>
              <th className="border border-gray-500 px-4 py-2">Action</th>
            </tr>
          </thead>
          <tbody>
            {courses.map((course) => (
              <tr key={course.id}>
                <td className="border border-gray-500 px-4 py-2">{course.id}</td>
                <td className="border border-gray-500 px-4 py-2">{course.name}</td>
                <td className="border border-gray-500 px-4 py-2">
                  <button className="mr-2 bg-blue-500 hover:bg-blue-600 text-white py-1 px-2 rounded" onClick={() => handleEdit(course.id)}>Edit</button>
                  <button className="bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded" onClick={() => handleDelete(course.id)}>Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ViewCourses;
