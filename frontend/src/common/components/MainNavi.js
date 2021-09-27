import React from "react"
import { Link } from "react-router-dom"
import styled from 'styled-components';

const MainNavi = () =>(
    <>
    <NaviList>
    <NaviItem><Link to='hook'>Hook</Link></NaviItem>
    <NaviItem><Link to='counter'>counter</Link></NaviItem>
    <NaviItem><Link to='todo'>Todo</Link></NaviItem>
    <NaviItem><Link to='algorithm-pages'>Algorithm</Link></NaviItem>
    
    <NaviItem><Link to='data-structure-pages' >DataStructure</Link></NaviItem>
    </NaviList>
    </>
)
export default MainNavi

const NaviList = styled.ul`
    display: flex;
    width: min-content;
    height:10px;
    margin: 30px
    
`

const NaviItem = styled.li`
    width: 110px;
    color: none;
    font-family: "ls";
    font-size: 0.5em;
    list-style: none;
    `