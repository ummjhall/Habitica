import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { createNewReward } from '../../redux/rewards';

function NewRewardField() {
  const dispatch = useDispatch();
  const [title, setTitle] = useState('');

  const handleNewReward = async (e) => {
    e.preventDefault();
    const newReward = { title, cost: 10 };
    if (title) {
      return dispatch(createNewReward(newReward)).then(setTitle(''));
    }
  };
  
  return (
    <form onSubmit={handleNewReward}>
      <input
        className="create-reward-input"
        placeholder={'Add a Reward'}
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      {/* <button type="submit">Create Reward</button> */}
    </form>
  );
}

export default NewRewardField;
