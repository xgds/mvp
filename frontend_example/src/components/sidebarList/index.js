import React from "react";
import { ListGroup, ListGroupItem } from 'reactstrap';

class SidebarList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            list:   [],
            active: [],
        };
        this.store = props.flightStore;
        this.content = props.content;
    }

    componentDidMount() {
        this.store.subscribe(() => (this.setState(
            {
                list: this.props.flightStore.getState().allFlights
            }
        )));
    }

    onClick(id) {
        if (this.state.active.includes(id))
        {
            this.setState(
                previousState => ({
                    active: previousState.active.filter((item) => (item != id))
                })
            );
            this.store.dispatch(
                {
                    type: "disable-flight",
                    flight: this.state.list[id]._id.$oid,
                }
            );
        } else {
            this.setState(
                previousState => ({
                    active: previousState.active.concat([id])
                })
            );
            this.store.dispatch(
                {
                    type: "enable-flight",
                    flight: this.state.list[id]._id.$oid,
                }
            );
        }
    }

    render() {
        let rArray = this.state.list.map((r, id) => (
            <ListGroupItem 
                key={id} 
                onClick={this.onClick.bind(this, id)}
                active={this.state.active.includes(id)}
                className="list-group-item"
            >
                <p className="header-item">{r._id.$oid.substring(r._id.$oid.length - 4)}</p>
                <p className="footer-item">{r.start.$date}</p>
                <p className="footer-item">{r.end.$date}</p>
            </ListGroupItem>
        ));
        return (
            <ListGroup className="listgroup">
                {rArray}
            </ListGroup>
        );
    }
}

export default SidebarList;