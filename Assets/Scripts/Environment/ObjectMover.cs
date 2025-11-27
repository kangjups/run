using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static UnityEngine.RuleTile.TilingRuleOutput;

// Time.delta Time : FPS 보정용( 지난 프레임이 완료되는 데 까지 걸리는 시간
public class ObjectMover : MonoBehaviour
{
    public float speed;
    void Update()
    {
        if (!GameManager.gameStarted) return;
        transform.position += Vector3.left * speed * Time.deltaTime; // left : (-1,0,0)
    }
}


/* move파이프를 오른쪽에서 왼쪽으로 움직이는 코드 
 * 기본제공 transform의 위치 x 좌표 변형 이때 fps 보정을 위해 time.deltatiem 사용
*/
