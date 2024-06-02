import React from 'react';
import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { SidebarButton } from "./button";


export interface TableData {
    headers: { key: string; label: string; className: string  }[];
    rows: { cells: { value: string; className?: string }[] }[];
}

export interface ButtonConfig {
    icon: any;
    variant: string;
    className: string;
    label: string;
}

interface CustomTableProps {
    data: TableData;
    buttons?: ButtonConfig[];
    additionalHeadings?: string[]; // Define an array of additional headings
}

const CustomTable: React.FC<CustomTableProps> = ({ data, buttons, additionalHeadings }) => {
    return (
        <div  className='mt-6'>
        <div className='mb-10 '>
            {additionalHeadings && (
                <div style={{ marginBottom: '10px' }}
                >
                    {additionalHeadings.map((heading, index) => (
                        <span key={index} style={{ marginRight: '10px' }}className='mb-10 text-3xl font-mono font-semibold'>{heading}</span>
                    ))}
                </div>
            )}
            </div>
            <div>
            <Table style={{ width: '100%', borderSpacing: '10px' }}>
                <TableCaption>A list of records</TableCaption>
                <TableHeader >
                    <TableRow>
                        {data.headers.map(header => (
                            <TableHead key={header.key} className={header.className} style={{ width: '150px' }}>{header.label}</TableHead>
                        ))}
                        {buttons && <TableHead>Action</TableHead>}
                    </TableRow>
                </TableHeader>
                <TableBody>
                    {data.rows.map((row, index) => (
                        <TableRow key={index}>
                            {row.cells.map((cell, cellIndex) => (
                                <TableCell key={cellIndex} className={cell.className}>{cell.value}</TableCell>
                            ))}
                            {buttons && (
                                <TableCell className="space-x-2">
                                    {buttons.map((Button, buttonIndex) => (
                                        <SidebarButton
                                            key={buttonIndex}
                                            icon={Button.icon}
                                            // variant={Button.variant}
                                            className={Button.className}
                                        >
                                            {Button.label}
                                        </SidebarButton>
                                    ))}
                                </TableCell>
                            )}
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            </div>
        </div>
    );
};

export default CustomTable;
