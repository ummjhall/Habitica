import { useSelector } from 'react-redux';
import { NavLink, useNavigate } from 'react-router-dom';
import ProfileButton from './ProfileButton';
import icon from '../../../dist/assets/imgs/questlog-icon3.jpg';
import './Navigation.css';

function Navigation() {
  const user = useSelector(state => state.session.user);
  const navigate = useNavigate();

  if (!user) return;

  return (
    <div className='nav-wrapper'>
      <div className='nav-wrapper_left'>
        <NavLink to='/'><img className='icon' src={icon} alt='icon' style={{width: '50px'}} /></NavLink>
        <div className='nav_app-name'>QuestLog</div>
        <div className='nav_link' onClick={() => navigate('/')}>
          <div className='nav_link_text'>Tasks</div>
        </div>
        <div className='nav_link' onClick={() => navigate('/equipment')}>
          <div className='nav_link_text'>Inventory</div>
        </div>
        <div className='nav_link' onClick={() => navigate('/shop')}>
          <div className='nav_link_text'>Shop</div>
        </div>
      </div>
      <ProfileButton />
    </div>
  );
}

export default Navigation;
