import { useState } from 'react';
import { postNewTask } from '../../redux/tasks';
import { useDispatch } from 'react-redux';

function NewHabitField() {
  const dispatch = useDispatch();
  const [title, setTitle] = useState('');

  const handleNewTask = async (e) => {
    e.preventDefault();

    const newTask = { title, type: 'habit' };
    if (title) {
      return dispatch(postNewTask(newTask)).then(setTitle(''));
    }
  };
  return (
    <form onSubmit={handleNewTask}>
      <label>
        <input
            className="create-habit-input"
          placeholder={'Add a Habit'}
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </label>
    </form>
  );
}

export default NewHabitField;
