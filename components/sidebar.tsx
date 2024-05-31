'use client'

import { SidebarItems } from "@/app/constant"
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from "@/components/ui/accordion"; // Import accordion components
import Link from "next/link";

interface SidebarProps {
    sidebarItems: SidebarItems;
}

export default function Sidebar({ sidebarItems }: SidebarProps) {
    return (
        <div className="w-[270px] max-w-xs h-screen fixed left-0 top-0 z-40 border-r overflow-y-auto">
            <div className="h-full px-3 py-4">
                <h3 className="mx-3 text-lg font-semibold text-foreground">
                    College
                </h3>
                <div className="mt-5">
                    <div className="flex flex-col gap-1 w-full">
                        {sidebarItems.links.map((link, index) => (
                            <div key={index}>
                                {link.submenu ? ( // Render SidebarItem with Accordion for items with submenus
                                    <Accordion type="single" collapsible>
                                        <AccordionItem value={index.toString()}> {/* Add a value property */}
                                            <AccordionTrigger>
                                                <div className="flex items-center w-full cursor-pointer">
                                                    {link.icon && <link.icon className="w-5 h-5 mr-2" />} {/* Render icon if provided */}
                                                    <span>{link.label}</span>
                                                </div>
                                            </AccordionTrigger>
                                            <AccordionContent>
                                                {link.submenu.map((submenuItem, subIndex) => (
                                                    <Link key={subIndex} href={submenuItem.href}>
                                                        <div className="flex items-center pl-4 cursor-pointer">
                                                            <span className="mb-2 hover:underline">{submenuItem.label}</span>
                                                        </div>
                                                    </Link>
                                                ))}
                                            </AccordionContent>
                                        </AccordionItem>
                                    </Accordion>
                                ) : ( // Render SidebarItem for items without submenus
                                  
                                        <div className="flex items-center cursor-pointer">
                                            {link.icon && <link.icon className="w-5 h-5 mr-2" />} {/* Render icon if provided */}
                                            <span>{link.label}</span>
                                        </div>
                                    
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}
