import { LucideIcon } from "lucide-react";

export interface SidebarItems {
  links: Array<{
    label: string;
    href?: string;
    icon?: LucideIcon;
    submenu?: Array<{
      label: string;
      href: string;
    }>;
  }>;
}


export interface Course {
  id: number;
  name: string;
}

export const courses: Course[] = [
  { id: 1, name: 'Course A' },
  { id: 2, name: 'Course B' },
  { id: 3, name: 'Course C' },
];



import { FilePenLine, Trash } from 'lucide-react';
import CustomTable, { ButtonConfig, TableData } from '@/components/custom-table';


    export const Coursedata: TableData = {
        headers: [
            { key: 'id', label: '#', className: 'w-[100px]' },
            { key: 'courseName', label: 'Course Name', className: 'w-[100px]' }
        ],
        rows: [
            { cells: [{ value: 'INV001', className: 'font-medium' }, { value: 'Bsc.CSIT' }] },
            { cells: [{ value: 'INV001', className: 'font-medium' }, { value: 'Bsc.CSIT' }] }
        ]
    };

    export const Coursebuttons: ButtonConfig[] = [
        { icon: FilePenLine, variant: 'default', className: 'bg-blue-600', label: 'Edit' },
        { icon: Trash, variant: 'destructive', className: 'bg-red-600', label: 'Delete' }
    ];
  
    export const Sessiondata: TableData = {
      headers: [
          { key: 'id', label: '#', className: 'w-[100px]' },
          { key: 'id', label: 'Start', className: 'w-[100px]' },
          { key: 'courseName', label: 'End', className: 'w-[100px]' }
      ],
      rows: [
          { cells: [{ value: 'INV001', className: 'font-medium' },{ value: 'Jan. 2, 2024', className: 'font-medium' }, { value: 'Dec. 30, 2024' }] },
          { cells: [{ value: 'INV001', className: 'font-medium' },{  value: 'Jan. 2, 2024', className: 'font-medium' }, { value: 'Dec. 30, 2024' }] }
      ]
  };

  export const Subjectdata: TableData = {
    headers: [
        { key: 'id', label: '#', className: 'w-[100px]' },
        { key: 'id', label: 'Subject', className: 'w-[100px]' },
        { key: 'TeacherName', label: 'Teacher', className: 'w-[100px]' },
        { key: 'CourseName', label: 'Course', className: 'w-[100px]' },
    ],
    rows: [
        { cells: [{ value: 'INV001', className: 'font-medium' },
        { value: 'Java', className: 'font-medium' },
        {  value: 'Steve Smith', className: 'font-medium' }, 
        { value: 'CSIT' }] },

        { cells: [{ value: 'INV001', className: 'font-medium' },
        {  value: 'Physics', className: 'font-medium' } ,
        {  value: 'Marnus', className: 'font-medium' },
        { value: 'BIT' }] }
    ]
};

export const Teacherdata: TableData = {
  headers: [
      { key: 'id', label: '#', className: 'w-[50px]' },
      { key: 'TeacherName', label: 'FullName', className: 'w-[50px]' },
      { key: 'Email', label: 'Email', className: 'w-[50px]' },
      { key: 'Gender', label: 'Gender', className: 'w-[50px]' },
      { key: 'CourseName', label: 'Course', className: 'w-[50px]' },
  ],
  rows: [
      { cells: [{ value: 'INV001' },
      {  value: 'Steve Smith',  }, 
      { value: 'smudge@gmail.com' },
      { value: 'M' },
      { value: 'CSIT' }
    ] },

      { cells: [{ value: 'INV001', className: 'font-medium' },
      {  value: 'Marnus', className: 'font-medium' },
      {  value: 'Physics', className: 'font-medium' } ,
      { value: 'M' },
      { value: 'BIT' }] }
  ]
};


export const Teacherbuttons: ButtonConfig[] = [
  { icon: FilePenLine, variant: 'default', 
  className: 'bg-blue-600', label: 'Edit',
  onClick: () => window.location.href = '/teacher/edit' },
  
  { icon: Trash, variant: 'destructive', className: 'bg-red-600', label: 'Delete' }
];

export const Studentdata: TableData = {
  headers: [
      { key: 'id', label: '#', className: 'w-[50px]' },
      { key: 'StudentName', label: 'FullName', className: 'w-[50px]' },
      { key: 'Email', label: 'Email', className: 'w-[50px]' },
      { key: 'Gender', label: 'Gender', className: 'w-[50px]' },
      { key: 'CourseName', label: 'Course', className: 'w-[50px]' },
  ],
  rows: [
      { cells: [{ value: 'INV001' },
      {  value: 'Steve Smith',  }, 
      { value: 'smudge@gmail.com' },
      { value: 'M' },
      { value: 'CSIT' }
    ] },

      { cells: [{ value: 'INV001', className: 'font-medium' },
      {  value: 'Marnus', className: 'font-medium' },
      {  value: 'Physics', className: 'font-medium' } ,
      { value: 'M' },
      { value: 'BIT' }] }
  ]
};
