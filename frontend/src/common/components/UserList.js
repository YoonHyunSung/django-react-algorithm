import React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import CommentIcon from '@mui/icons-material/Comment';
import {useSelector, useDispatch} from 'react-redux'
import { todoReducer } from 'reducers';
import { deleteEmailAction } from 'reducers/user.reducer';


const UserList = () =>{
    const dispatch = useDispatch()
    const deleteEmail = email => dispatch(deleteEmailAction(email))
    
    const users = useSelector(state => state.userReducer.users)
    return(<>
            <h1>{console.log(users)}</h1>
            {users.length === 0 &&(<h1>인원이없습니다</h1>)}
            {users.length !== 0 && (<h1>{users.length} 명의 인원</h1>)}
            {users.length !== 0 && users.map(
                user =>(<div key={user.email}>
                    {user.complete ? 
                    <span style={{textDecoration:'line-through'}}>{user.email}</span>
                    :<span>{user.email}</span>}
                    <button onClick ={deleteEmail.bind(null, user.email)}>x</button>
                </div>)
            )}
            
            
    </>)

}
export default UserList