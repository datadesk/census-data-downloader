# TABLE INVENTORY

All of the U.S. Census tables processed by this library.

<table>
<thead>
    <tr>
        <th>Slug</th>
        <th>Universe</th>
        <th>Raw table</th>
    </tr>
</thead>
<tbody>
    {% for obj in object_list %}
        <tr>
            <td>{{ obj.PROCESSED_TABLE_NAME }}</td>
            <td>{{ obj.UNIVERSE }}</td>
            <td>{{ obj.RAW_TABLE_NAME }}</td>
        </tr>
    {% endfor %}
</tbody>
</table>
