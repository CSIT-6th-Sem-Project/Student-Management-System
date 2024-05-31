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
