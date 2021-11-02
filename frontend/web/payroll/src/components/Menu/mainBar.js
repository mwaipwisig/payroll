import React from 'react'
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import {IconContext} from "react-icons";
const Nav = styled.div`
    background:#497;
    height:13vh;
    display:flex;
    justify-content:flex-start;
    align-items:center;
    position: relative;  
    top: 0;
  z-index: 0;
  
`;
const NavIcon = styled(Link)`
  margin-left: 2rem;
  font-size: 2rem;
  height: 80px;
  display: flex;
  justify-content: flex-start;
  align-items: center;  
`;

const mainBar = ()=>{
    return <>

    <IconContext.Provider>
                <Nav>
            <NavIcon to='#'>
                <span className='fa fa-bars'/>
            </NavIcon>


        </Nav>
    </IconContext.Provider>
    </>
}
export default mainBar;