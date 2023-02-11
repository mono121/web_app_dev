import React, { useState } from 'react';
import { useCookies } from 'react-cookie';
import axios from 'axios';
import { useForm } from "react-hook-form";

const apiURL = 'http://localhost:8000/api/';

const Login = (props) => {

    const [cookies, setCookie] = useCookies();
    const { register, handleSubmit, watch, errors } = useForm();

    const getJwt = async (data) =>{
        await axios.post(`${apiURL}auth/jwt/create/`,
          {
            username:"admin",
            password:"password",
          },
        )
        .then(function (response) {
          console.log(response.data.access)
          setCookie('accesstoken', response.data.access, { path: '/' }, { httpOnly: true });
          setCookie('refreshtoken', response.data.refresh, { path: '/' }, { httpOnly: true });
        })
        .catch(err => {
            console.log("miss");
            alert("usernameかPasswordが違います");
        });
      };

    const [tasks, setTasks] = useState([])

    const getTasks = () =>{
        axios.get(`${apiURL}tasks/`, {
          headers: {
            Authorization : `JWT ${cookies.accesstoken}`,
          }
        })
        .then(res => {setTasks(res.data)})
        console.log(`JWT ${cookies.accesstoken}`)
    }

    return (
        <div className="top-wrapper">
          <div className="login">
            <h3>Login</h3>
          </div>
          <div className="login-block">
            <form onSubmit={handleSubmit(getJwt)}>
              <label for="username">Username：</label>
              <input className='form-control' {...register('username')} />
              <label for="password">PassWord：</label>
              <input className='form-control' type="password" {...register('password', { required: true })} />
              <input className='btn btn-secondary' type="submit" value="ログイン" />
            </form>
            <button onClick={getTasks}>Show Tasks</button>
            <div>
                <ul>
                {
                  tasks.map(task => <li key={task.id}> ID : {task.id}, Title : {task.title}</li>)
                }
                </ul>
            </div>
          </div>
        </div>
    );
  }

  export default Login;