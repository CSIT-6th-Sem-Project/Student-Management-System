"use client"

import { Book, BookOpenCheck, Clock, UserRound, UsersRound } from "lucide-react"
import Sidebar from "./sidebar"

export function MainSidebar(){
    return(
        <Sidebar  sidebarItems={{
            links:[
              {label:'Course', 
              icon:BookOpenCheck,
               submenu: [
                { label: "View Courses", href: "/courses" },
                { label: "Add Course", href: "/courses/add" },
                { label: "Edit Course", href: "/courses/edit" },
              ],},

              {label:'Subject',
               icon:Book, 
               submenu: [
                { label: "View Subject", href: "/subject" },
                { label: "Add  Subject", href: "/subject/add" },
                { label: "Edit  Subject", href: "/subject/edit" },
              ],},

              {label:'Session',
              icon:Clock,
               submenu: [
                { label: "View Session", href: "/session" },
                { label: "Add Session", href: "/session/add" },
                { label: "Edit Session", href: "/session/edit" },
              ],},

              {label:'Teacher',
               icon:UserRound,
                submenu: [
                { label: "View Teacher", href: "/teacher" },
                { label: "Add Teacher", href: "/teacher/add" },
                { label: "Edit Teacher", href: "/teacher/edit" },
              ],},

              {label:'Students', 
              icon:UsersRound,
               submenu: [
                { label: "View Students", href: "/student" },
                { label: "Add Students", href: "/student/add" },
                { label: "Edit Students", href: "/student/edit" },
              ],},
            ]
          }}/>
    )
}