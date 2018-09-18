import React from "react";
import { ListGroup, ListGroupItem } from 'reactstrap';

class SidebarList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            list: props.list,
            active: [],
        };
        this.store = props.store;
        this.content = props.content;
    }

    onClick(id) {
        if (this.state.active.includes(id))
        {
            this.setState(
                previousState => ({
                    active: previousState.active.filter((item) => (item != id))
                })
            );
            if (this.content == "flights")
            {
                this.store.dispatch(
                    {
                        type: "disable-flight",
                        flight: id,
                    }
                );
            }
        } else {
            this.setState(
                previousState => ({
                    active: previousState.active.concat([id])
                })
            );
            if (this.content == "flights")
            {
                this.store.dispatch(
                    {
                        type: "enable-flight",
                        flight: id,
                    }
                );
            }
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
            <p className="header-item">{r}</p>
            <p className="footer-item">15:55 05/06/2018</p>
            <p className="footer-item">18:20 06/06/2018</p>
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