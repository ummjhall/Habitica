import OpenModalTaskItem from './OpenModalTaskItem';
import EditTaskModal from '../EditTaskModal/EditTaskModal';
import './TaskItemTile.css';
import TaskItemCheckoff from './TaskItemCheckoff';

function TaskItemTile({ user, task, avatar }) {
  const getBackgroundColor = () => {
    switch (task?.difficulty) {
      case 1:
        return '#26CC8F';
      case 2:
        return '#FFBF5D';
      case 3:
        return '#FF944C';
      case 4:
        return '#d95050';
      default:
        return 'transparent';
    }
  };

  return (
    <div className="taskItemTile">
      <div
        className="checkbox-container"
        style={{ backgroundColor: getBackgroundColor() }}
      >
        <TaskItemCheckoff
          className="check-off"
          user={user}
          task={task}
          avatar={avatar}
        />
      </div>
      <div className="taskModalButton">
        <OpenModalTaskItem
          itemText={task.title}
          modalComponent={<EditTaskModal user={user} task={task} className='taskModalClick'/>}
          customClass={'taskModalButton'}
          task={task}
        />
      </div>
    </div>
  );
}

export default TaskItemTile;
