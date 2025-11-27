// 스크립트 이름: RotateObstacle.cs
using UnityEngine;

public class RotateObstacle : MonoBehaviour
{
    public float rotateSpeed = 100f; // 회전 속도 (음수면 반대 방향)

    void Update()
    {
        if (!GameManager.gameStarted) return;

        // Z축을 기준으로 회전
        transform.Rotate(0, 0, rotateSpeed * Time.deltaTime);
    }
}