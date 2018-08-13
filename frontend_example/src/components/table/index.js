import style from "./style.css";
import React from "react";

class Table extends React.Component {
    render() {
        return <div className={style.primary}>
            Hello Table Component!
        </div>;
    }
}

export default Table;