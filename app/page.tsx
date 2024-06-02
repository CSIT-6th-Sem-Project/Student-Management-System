"use client"

import { Users } from 'lucide-react';
import React, { PureComponent } from 'react';
import {  FaArrowCircleRight, FaUserGraduate,FaUsers  } from "react-icons/fa";
import { FaBook } from "react-icons/fa6";
import { BsFillGrid1X2Fill } from "react-icons/bs";
import Link from 'next/link';

export default function Home() {
  return (
    <main className="mr-auto" >
      <p className='text-3xl font-bold mt-5'>Admin Dashboard</p>
      <div className="container px-4 py-6 grid grid-cols-12 gap-4" >
    <div className="bg-blue-400 h-32 rounded-lg col-span-12 md:col-span-6 lg:col-span-3 mb-4">
      <div className='flex flex-row justify-between'>
      <div className='ml-5'>
      <p className='text-5xl font-serif'>1</p>
      <p className='font-serif mt-2'>Total Students</p>
      </div>
      <div className="relative">
      <FaUserGraduate className="ml-auto mr-4 text-7xl mt-6 opacity-30 
      transition-all duration-300 transform hover:scale-110 
        hover:shadow-lg" />
     </div>
      </div>
      <div className='bg-blue-900 mt-4   flex items-center justify-center'>
  <p >More info</p>
  <Link href='/student' ><FaArrowCircleRight  /></Link>
</div>
    </div>

<div className="bg-green-600 h-32 rounded-lg mb-4 col-span-12 md:col-span-6 lg:col-span-3">
      <div className='flex flex-row justify-between'>
      <div className='ml-5'>
      <p className='text-5xl font-serif'>1</p>
      <p className='font-serif mt-2'>Total Teachers</p>
      </div>
      <div className="relative">
      <FaUsers  className="ml-auto mr-4 text-7xl mt-6 opacity-30 
      transition-all duration-300 transform hover:scale-110 
        hover:shadow-lg" />
     </div>
      </div>
      <div className='bg-green-900 mt-4   flex items-center justify-center'>
  <p >More info</p>
  <Link href='/student' ><FaArrowCircleRight  /></Link>
</div>
    </div>

    <div className="bg-purple-600 h-32 rounded-lg mb-4 col-span-12 md:col-span-6 lg:col-span-3">
      <div className='flex flex-row justify-between'>
      <div className='ml-5'>
      <p className='text-5xl font-serif'>1</p>
      <p className='font-serif mt-2'>Total Course</p>
      </div>
      <div className="relative">
      <BsFillGrid1X2Fill  className="ml-auto mr-4 text-7xl mt-6 opacity-30 
      transition-all duration-300 transform hover:scale-110 
        hover:shadow-lg" />
     </div>
      </div>
      <div className='bg-purple-900 mt-4   flex items-center justify-center'>
  <p>More info</p>
  <Link href='/student' ><FaArrowCircleRight  /></Link>
</div>
    </div>

    <div className="bg-red-500 h-32 rounded-lg mb-4 col-span-12 md:col-span-6 lg:col-span-3">
      <div className='flex flex-row justify-between'>
      <div className='ml-5'>
      <p className='text-5xl font-serif'>1</p>
      <p className='font-serif mt-2'>Total Subjects</p>
      </div>
      <div className="relative">
      <FaBook className="ml-auto mr-4 text-7xl mt-6 opacity-30 
      transition-all duration-300 transform hover:scale-110 
        hover:shadow-lg" />
     </div>
      </div>
      <div className='bg-red-700 mt-4  flex items-center justify-center'>
  <p >More info</p>
  <Link href='/student' ><FaArrowCircleRight  /></Link>
</div>
    </div>
</div>
    </main>
  );
}
