using UnityEngine;

public class ScoreTrigger : MonoBehaviour
{
    // [추가] 인스펙터에서 오디오 클립을 넣을 수 있게 변수 선언
    public AudioClip scoreSound;

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            ScoreManager.Instance.AddScore(1);

            // [추가] 소리가 설정되어 있다면 재생!
            if (scoreSound != null)
            {
                // 2D 사운드 재생 (위치 상관없이 들림)
                AudioSource.PlayClipAtPoint(scoreSound, Camera.main.transform.position);
            }
        }
    }
}