import './App.css';
import SideBar from './components/SideBar';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import home from './pages/home'
import about from './pages/about'
import { Projects, ProjectOne, ProjectTwo } from './pages/projects';
import contact from './pages/contact'
import extra from './pages/extra';

function App() {
  return (
    <Router>
    <SideBar />
    <Switch>
      <Route path="/home" exact component={home}/>
      <Route path="/home/about" exact component={about}/>
      <Route path="/home/contact" exact component={contact}/>
      <Route path="/projects" exact component={Projects}/>
      <Route path='/projects/projects1' exact component={ProjectOne} />
      <Route path='/projects/projects2' exact component={ProjectTwo} />
      <Route path='/extra' exact component={extra} />
    </Switch>
    </Router>
  );
}

export default App;
