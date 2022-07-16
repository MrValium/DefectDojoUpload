def zap_get_alerts(zap, baseurl, denylist, out_of_scope_dict):
    st = 0
    pg = 5000
    false_positives = [(10096, 'http://example.com'),(10021,'http://192.168.49.2:31190/swagger-ui/swagger-ui.css'),(10038,'http://192.168.49.2:31190/'),(10038,'http://192.168.49.2:31190')]
    alerts = zap.core.alerts(baseurl=baseurl, start=st, count=pg)
    logging.debug('AAAAAAAAAAAAA')
    logging.debug(alerts)
    while len(alerts) > 0:
        for alert in alerts:
            alert_id = alert.get('id')
            url = alert.get('url')
            plugin_id = alert.get('pluginId')
            
            for fp in false_positives:
                if plugin_id == fp[0] and url == fp[1]:
                    zap.alert.update_alerts_confidence(alert_id, 'PASS')
        st += pg
        alerts = zap.core.alerts(start=st, count=pg)
    return alerts
