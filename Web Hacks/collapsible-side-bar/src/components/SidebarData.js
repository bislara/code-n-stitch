import React from "react";
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

export const SidebarData = [
    {
        title: 'Home',
        path: '/home',
        icon: <AiIcons.AiFillHome />,
        iconClosed: <RiIcons.RiArrowDownSFill />, 
        iconOpened: <RiIcons.RiArrowUpSFill />,
        subNav: [
            {
            title: 'About',
            path: '/home/about',
            icon: <IoIcons.IoIosPaper />,
            },
            {
            title: 'Contact Us',
            path: '/home/contact',
            icon: <AiIcons.AiFillPhone />,
            },
        ]
    },
    {
        title: 'Projects',
        path: '/projects',
        icon: <AiIcons.AiFillHome />,
        iconClosed: <RiIcons.RiArrowDownSFill />, 
        iconOpened: <RiIcons.RiArrowUpSFill />,
        subNav: [
            {
            title: 'Project 1',
            path: '/projects/projects1',
            icon: <IoIcons.IoIosPaper />,
            },
            {
            title: 'Reports 2',
            path: '/projects/projects2',
            icon: <IoIcons.IoIosPaper />,
            }
        ]
    },
    {
        title:'Extra', 
        path: '/extra',
        icon: <AiIcons.AiFillSmile/>,

    }
]