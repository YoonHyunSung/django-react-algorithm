

const initialState = {users:[], user:{}}
export const addUserAction = user =>({type: "ADD_USER", payload: user})
export const deleteEmailAction = todoId =>({type:'DELETE_EMAIL', payload:todoId})
const userReducer = (state =initialState, action) =>{
    switch(action.type){
        case 'ADD_USER' : return {...state, users:[...state.users, action.payload]}
        case 'DELETE_EMAIL' : return{...state, users:state.users.filter(user =>user.email !=action)}
        default : return state
        
    }
}
export default userReducer