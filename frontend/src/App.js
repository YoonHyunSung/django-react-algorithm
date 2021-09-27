import {Route, Switch, Redirect } from 'react-router-dom';
import { DynamicConquer,
        Greedy, DivideConquer, BruteForce, BackTracking, AlgorithmPages, AlgorithmNavi} 
        from 'algorithm/index';
import {DataStructureNavi, DataStructurePages, Linear, NonLinear} from 'dataStructure/index'
import {Counter, Home, MainNavi, SignIn, Todo} from 'common/index'


const App = () => {
  return(
 <> 
  <MainNavi/>
  <Switch>
        <Route exact path='/' component= { Home }/>
        <Redirect from='/home' to= { '/' }/>
        <Route exact path='/sign-in' component={SignIn}/>
        <Route exact path='/counter' component={Counter}/>
        <Route exact path='/todo' component={Todo}/>
        <Route exact path='/data-structure-navi' component={DataStructureNavi}/>

        <Route exact path='/algorithm-pages' component={AlgorithmPages}/>
        <Route exact path='/algoritm-navi' component={AlgorithmNavi}/>
        <Route exact path='/dynamic-conquer' component={DynamicConquer}/>
        <Route exact path='/greedy' component={Greedy}/>
        <Route exact path='/divide-conquer' component={DivideConquer}/>
        <Route exact path='/brute-force' component={BruteForce}/>
        <Route exact path='/back-tracking' component={BackTracking}/>

        <Route exact path='/data-structure-pages' component={DataStructurePages}/>

        <Route exact path='/linear' component={Linear}/>
        <Route exact path='/non-linear' component={NonLinear}/>
        <Route exact path='/math' component={Math}/>


  </Switch>

  </>
  )
};
export default App;
